import math

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

class Kruh(Shape):
    def __init__(self, polomer=0):
        super().__init__()
        self.polomer = polomer
        print("Vytvarim kruh")

    def obvod(self):
        return 2 * math.pi * self.polomer

    def obsah(self):
        return math.pi * self.polomer ** 2

    def ziskej_polomer(self):
        return self.polomer

    def info(self):
        print(f"Kruh s polomerem {self.polomer}")

class Valec(Kruh):
    def __init__(self, polomer=0, vyska=0):
        super().__init__(polomer)
        self.vyska = vyska
        print("Vytvarim valec")

    def objem(self):
        return math.pi * self.ziskej_polomer() ** 2 * self.vyska

    def info(self):
        print(f"Valec s polomerem {self.ziskej_polomer()} a vyskou {self.vyska}")

class Koule(Kruh):
    def __init__(self, polomer=0):
        super().__init__(polomer)
        print("Vytvarim kouli")

    def objem(self):
        return (4 / 3) * math.pi * self.ziskej_polomer() ** 3

    def info(self):
        print(f"Koule s polomerem {self.ziskej_polomer()}")

def main():
    rec = Rectangle()
    rec1 = Rectangle(5, 6)

    cb = Cube(5)
    print(cb.volume())
    cb.print_info()

    kr = Kruh(3)
    print(kr.obvod())
    print(kr.obsah())
    kr.info()

    val = Valec(3, 4)
    print(val.objem())
    val.info()

    gul = Koule(2)
    print(gul.objem())
    gul.info()


if __name__ == "__main__":
    main()
