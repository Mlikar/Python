class Shape:
    def __init__(self):
        print("Vykresluji obrazec")

class Square(Shape):
    def __init__(self, a=0):
        super().__init__()
        self.a = a
        print("Vytvarime ctverec")

    def perimeter(self):
        return self.a * 4

    def content(self):
        return self.a * self.a

    def print_info(self):
        print(f"Ctverec se stranou o delce {self.a}")

class Rectangle(Square):
    def __init__(self, a=0, b=0):
        super().__init__(a)
        self.b = b
        print("Vytvarime obdelnik")

    def perimeter(self):
        return 2 * self.b + 2 * self.a

    def content(self):
        return self.b * self.a

    def print_info(self):
        print(f"Obdelnik se stranou o delce {self.a} a druhou stranou o delce {self.b}")

class Cube(Square):
    def __init__(self, a=0):
        super().__init__(a)
        print("Vytvarime kostku")

    def volume(self):
        return self.content() * self.a

    def print_info(self):
        print(f"Kostka se stranami o delce {self.a}")


def main():
    rec = Rectangle()
    rec1 = Rectangle(5, 6)

    cb = Cube(5)
    print(cb.volume())
    cb.print_info()


if __name__ == "__main__":
    main()
