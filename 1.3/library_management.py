# DigolTech — Python Internship Assessment
# Section C: Coding Assessment — OOP & Functions
# Q1. Library Management System


class Book:
    """Represents a single book in the library."""

    def __init__(self, book_id, title, author, is_available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = is_available

    def display_details(self):
        status = "Available" if self.is_available else "Issued"
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")


class Library:
    """Manages a collection of Book objects and library operations."""

    def __init__(self):
        self.books = []

    def search_book(self, book_id):
        """Find and return a Book object by its ID, or None if not found."""
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def add_book(self, book):
        """Add a new book if its book_id is unique."""
        if self.search_book(book.book_id) is not None:
            print("Error: Book ID already exists!")
            return False

        self.books.append(book)
        print("Book added successfully!")
        return True

    def view_books(self):
        """Display all books currently in the library."""
        if not self.books:
            print("No books available in the library.")
            return

        print("========== BOOK LIST ==========")
        for index, book in enumerate(self.books):
            print()
            book.display_details()
            if index < len(self.books) - 1:
                print()
                print("-------------------------------")

    def issue_book(self, book_id):
        """Issue an available book by its ID."""
        book = self.search_book(book_id)
        if book is None:
            print("Error: Book not found!")
            return False

        if not book.is_available:
            print("Sorry! This book is already issued.")
            return False

        book.is_available = False
        print("Book issued successfully!")
        return True

    def return_book(self, book_id):
        """Return an issued book by its ID."""
        book = self.search_book(book_id)
        if book is None:
            print("Error: Book not found!")
            return False

        if book.is_available:
            print("Error: This book was not issued.")
            return False

        book.is_available = True
        print("Book returned successfully!")
        return True


def get_valid_int(prompt):
    """Safely read an integer value from user input."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input! Please enter a valid numeric ID.")


def display_menu():
    """Print the main menu options."""
    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")


def main():
    """Run the menu-driven Library Management System."""
    library = Library()

    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            book_id = get_valid_int("\nEnter Book ID: ")
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()

            if not title or not author:
                print("Error: Book title and author name cannot be empty.")
                continue

            new_book = Book(book_id, title, author)
            print()
            library.add_book(new_book)

        elif choice == "2":
            print()
            library.view_books()

        elif choice == "3":
            book_id = get_valid_int("\nEnter Book ID: ")
            book = library.search_book(book_id)
            print()
            if book is not None:
                print("Book Found!\n")
                book.display_details()
            else:
                print("Error: Book not found!")

        elif choice == "4":
            book_id = get_valid_int("\nEnter Book ID: ")
            print()
            library.issue_book(book_id)

        elif choice == "5":
            book_id = get_valid_int("\nEnter Book ID: ")
            print()
            library.return_book(book_id)

        elif choice == "6":
            print("\nExiting Library Management System. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please select an option from 1 to 6.")


if __name__ == "__main__":
    main()
