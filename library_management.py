class Library:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        for book in books:
            book_info = book.strip().split(',')
            print(f"Book Title: {book_info[0]}, Author: {book_info[1]}, Release Year: {book_info[2]}, Number of pages: {book_info[3]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        release_year = input("Enter release year: ")
        pages = input("Enter number of pages: ")

        self.file.seek(0)
        books = self.file.readlines()
        for book in books:
            book_info = book.strip().split(',')
            if title == book_info[0] and author == book_info[1]:
                print("Book already exists in the library.")
                return  # Exit the method if book already exists

        book_info = f"{title},{author},{release_year},{pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ").strip()
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        for book in books:
            if title not in book:
                updated_books.append(book)
        self.file.seek(0)
        self.file.truncate()
        for book in updated_books:
            self.file.write(book)
        print(f"Book with title '{title}' removed successfully.")


# Creating an object named "lib" with the Library class
lib = Library("books.txt")

# Menu
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
