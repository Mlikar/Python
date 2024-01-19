class Book:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.author = ""
        self.available = False

    def __init__(self, book_str: str):
        information = book_str.split(';')
        self.id = int(information[0])
        self.name = information[1]
        self.author = information[2]
        self.available = information[3] == "Available"

    def get_id(self) -> int:
        return self.id

    def set_id(self, book_id: int):
        self.id = book_id

    def get_available(self) -> bool:
        return self.available

    def set_available(self, available: bool):
        self.available = available

    def get_name(self) -> str:
        return self.name

    def __lt__(self, other):
        return self.author < other.author

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        availability = "Available" if self.available else "Unavailable"
        return f"{self.id};{self.name};{self.author};{availability}"

    def __repr__(self):
        return f"Book('{self.id}', '{self.name}', '{self.author}', '{self.available}')"

    def __del__(self):
        pass  # Destructor not needed in Python

def main():
    # Example usage of the Book class
    book_str = "9;Animal Farm;Orwell George;Available"
    book = Book(book_str)
    print(book)

if __name__ == "__main__":
    main()
