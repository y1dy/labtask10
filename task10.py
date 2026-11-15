class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_quantity = quantity
        self.available_quantity = quantity


class Library:
    def __init__(self):
        # Dictionary to store books {book_id: Book_object}
        self.books = {}
        # List of dictionaries to store issued book records
        self.issued_books = []

    def add_book(self):
        print("\nADD NEW BOOK")
        book_id = input("Enter Book ID: ").strip()
        if not book_id:
            print("Book ID cannot be empty.")
            return
        if book_id in self.books:
            print("Error: Book ID already exists! Must be unique.")
            return

        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()
        qty_input = input("Enter Quantity: ").strip()

        if not qty_input.isdigit() or int(qty_input) <= 0:
            print("Error: Quantity must be a positive whole number.")
            return

        quantity = int(qty_input)
        self.books[book_id] = Book(book_id, title, author, quantity)
        print("Book added successfully!")

    def view_all_books(self):
        print("\n--- ALL BOOKS ---")
        if not self.books:
            print("No books in the library.")
            return

        for book in self.books.values():
            print(
                f"ID: {book.book_id} | Title: {book.title} | Author: {book.author} | "
                f"Available: {book.available_quantity}/{book.total_quantity}"
            )

    def search_book(self):
        print("\nSEARCH BOOK")
        query = input("Enter Book ID or Title: ").strip().lower()
        found = False

        for book in self.books.values():
            if book.book_id.lower() == query or query in book.title.lower():
                print(
                    f"Found -> ID: {book.book_id} | Title: {book.title} | "
                    f"Author: {book.author} | Available: {book.available_quantity}"
                )
                found = True

        if not found:
            print("Book not found.")

    def issue_book(self):
        print("\nISSUE BOOK")
        book_id = input("Enter Book ID: ").strip()
        if book_id not in self.books:
            print("Error: Book ID not found.")
            return

        book = self.books[book_id]
        if book.available_quantity <= 0:
            print("Error: Book is currently unavailable (Available Quantity: 0).")
            return

        student_name = input("Enter Student Name: ").strip()
        if not student_name:
            print("Error: Student name cannot be empty.")
            return

        book.available_quantity -= 1
        self.issued_books.append({
            "book_id": book.book_id,
            "title": book.title,
            "student": student_name
        })
        print("Book issued successfully!")
        print(f"Available Quantity: {book.available_quantity}")

    def return_book(self):
        print("\nRETURN BOOK")
        book_id = input("Enter Book ID: ").strip()
        student_name = input("Enter Student Name: ").strip()

        for record in self.issued_books:
            if record["book_id"] == book_id and record["student"].lower() == student_name.lower():
                self.issued_books.remove(record)
                self.books[book_id].available_quantity += 1
                print("Book returned successfully!")
                print(f"Available Quantity: {self.books[book_id].available_quantity}")
                return

        print("Error: No matching issued record found for this book and student.")

    def delete_book(self):
        print("\nDELETE BOOK")
        book_id = input("Enter Book ID to delete: ").strip()
        if book_id not in self.books:
            print("Error: Book ID not found.")
            return

        book = self.books[book_id]
        if book.available_quantity < book.total_quantity:
            print("Error: Cannot delete book while copies are issued to students.")
            return

        del self.books[book_id]
        print("Book deleted successfully!")

    def view_issued_books(self):
        print("\n--- ISSUED BOOKS ---")
        if not self.issued_books:
            print("No books are currently issued.")
            return

        for record in self.issued_books:
            print(
                f"Book ID: {record['book_id']} | Title: {record['title']} | "
                f"Issued To: {record['student']}"
            )


def main():
    library = Library()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. View Issued Books")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_all_books()
        elif choice == "3":
            library.search_book()
        elif choice == "4":
            library.issue_book()
        elif choice == "5":
            library.return_book()
        elif choice == "6":
            library.delete_book()
        elif choice == "7":
            library.view_issued_books()
        elif choice == "8":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1 and 8.")


if __name__ == "__main__":
    main()