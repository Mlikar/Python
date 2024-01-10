from typing import List
from Book import Book  # Assuming Book class is defined in Book.py
from io import StringIO

class Library:
    def __init__(self, path_to_file: str):
        self.path = path_to_file
        self.books = []
        self.load_books_from_file()
        self.sort_books()

    def load_books_from_file(self):
        try:
            with open(self.path, 'r') as file:
                for line in file:
                    self.books.append(Book(line.strip()))
        except FileNotFoundError:
            # Handle the case when the file is not found
            print(f"File '{self.path}' not found. Creating an empty library.")

    def sort_books(self):
        self.books.sort()

    def get_available_books(self) -> List[Book]:
        return [book for book in self.books if book.get_available()]

    def add_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)
            self.sort_books()
            print(f"Kniha přidána s ID: {book.get_id()}")
        else:
            print("Kniha nemá unikátní ID")

    def get_unique_id(self) -> int:
        last_id = max(book.get_id() for book in self.books) if self.books else 0
        return last_id + 1

    def show_available_books(self):
        for book in self.get_available_books():
            print(book)

    def find_book_and_borrow_it(self, name: str):
        available_books = [book for book in self.get_available_books() if name.lower() in book.get_name().lower()]

        if len(available_books) > 1:
            print("Nalezena více knih, prosím upřesněte hledání:")
            for book in available_books:
                print(book)
        elif len(available_books) < 1:
            print("Nenalezena žádná dostupná kniha s tímto jménem.")
        else:
            print("Nalezena tato kniha:")
            print(available_books[0])
            borrow = input("Chcete knihu vypůjčit? (A/N): ").strip().upper()
            if borrow == 'A':
                available_books[0].set_available(False)
                print("Kniha vypůjčena")

    def __str__(self):
        return '\n'.join(str(book) for book in self.books)

    def __del__(self):
        with open(self.path, 'w') as file:
            file.write(str(self))

def main():
    # Example usage of the Library class
    library = Library("data.txt")
    print(library, end='\n\n')

    book = Book("9;Animal Farm;Orwell George;Available")
    library.add_book(book)
    print()

    book.set_id(library.get_unique_id())
    library.add_book(book)
    print()

    print("Dostupné knihy:")
    library.show_available_books()
    print()

    print("Půjčení knihy:")
    library.find_book_and_borrow_it("Kill")
    print()
    library.find_book_and_borrow_it("a")
    print()
    library.find_book_and_borrow_it("Great")
    print()

    print("Dostupné knihy:")
    library.show_available_books()
    print()

if __name__ == "__main__":
    main()
