from library import Library

if __name__ == "__main__":
    library = Library()

    # Adding Books
    library.add_book("Tolkāppiyam", "Tholkappiyar")
    library.add_book("Cilappatikaram", "Ilango Adigal")
    library.add_book("Sila Nerangalil sila Manithargal", "Jayakanthan")
    library.add_book("Aram", "Jeyamohan")
    library.add_book("Ponniyin Selvan", "Kalki")
    library.add_book("Parthiban Kanavu", "Kalki")

    # Registering Users
    library.register_user("Ruthra")
    library.register_user("Ruthravarshan")
    library.register_user("Varshan")

    # Borrowing Books
    library.borrow_book("1", "1")  # Rutrha borrows "Tolkāppiyam"
    library.borrow_book("2", "2")  # Ruthravarshan borrows "Cilappatikaram"

    # Returning Books
    library.return_book("1", "1")  # Rutrha returns "Tolkāppiyam"
