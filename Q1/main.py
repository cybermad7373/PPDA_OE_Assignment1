from library import Library

if __name__ == "__main__":
    library = Library()

    # Adding Books
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("1984", "George Orwell")

    # Registering Users
    library.register_user("Alice")
    library.register_user("Bob")

    # Borrowing Books
    library.borrow_book("1", "1")  # Alice borrows "The Great Gatsby"
    library.borrow_book("2", "2")  # Bob borrows "1984"

    # Returning Books
    library.return_book("1", "1")  # Alice returns "The Great Gatsby"
