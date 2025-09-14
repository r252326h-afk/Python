# =========================
# Number 1: Inheritance + overriding
# =========================
class Vehicle:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def description(self) -> str:
        return f"{self.make} {self.model}"

    def start(self) -> str:
        return f"{self.description()}: starting generic vehicle..."


class Car(Vehicle):
    def start(self) -> str:
        # override the base method
        return f"{self.description()}: engine roars — car is ready!"


class Bike(Vehicle):
    def start(self) -> str:
        # override the base method with bike-specific behavior
        return f"{self.description()}: pedaling engaged — bike is rolling!"


c = Car("Toyota", "Corolla")
b = Bike("Trek", "FX 3")
print(c.start())
print(b.start())

# =========================
# Number 2: Polymorphism with area()
# =========================
import math
from typing import List

class Shape:
    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement area()")


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


def total_area(shapes: List[Shape]) -> float:
    return sum(s.area() for s in shapes)


items = [Circle(2), Rectangle(3, 4), Circle(1)]
print("Total area:", total_area(items))

# =========================
# Number 3: Calling super().__init__ inside a method (non-idiomatic, but per brief)
# =========================
class BaseShape:
    def __init__(self, color: str = "transparent"):
        self.color = color
        print(f"BaseShape.__init__ called: color={self.color}")

    def calculate_area(self) -> float:
        return 0.0


class FancyRectangle(BaseShape):
    def __init__(self, width: float, height: float, color: str | None = None):
        # Intentionally NOT calling super().__init__ here (to demonstrate calling it later)
        self.width = width
        self.height = height
        if color is not None:
            super().__init__(color)  # optional immediate init if color provided

    def calculate_area(self) -> float:
        # Ensure parent initialization has happened; call it here if needed
        if not hasattr(self, "color"):
            super().__init__(color="blue")  # late init via super()
            print("Called BaseShape.__init__ from FancyRectangle.calculate_area()")
        return self.width * self.height


rect = FancyRectangle(5, 4)  # no color set here
area = rect.calculate_area()  # triggers late super().__init__()
print("FancyRectangle area:", area)
print("FancyRectangle color after ensure:", rect.color)

# =========================
# Number 4: Duck typing / Protocol-based polymorphism
# =========================
from typing import Protocol

class SoundMaker(Protocol):
    def make_sound(self) -> str: ...

class Dog:
    def make_sound(self) -> str:
        return "Woof"

class Cat:
    def make_sound(self) -> str:
        return "Meow..."

def process_sound(sound_object: SoundMaker) -> None:
    s = sound_object.make_sound()
    print(f"Processed sound: {s}")

d = Dog()
c = Cat()
process_sound(d)
process_sound(c)

# =========================
# Script entry point example
# =========================
def print_hi(name: str) -> None:
    print(f"Hi, {name}")

if __name__ == "__main__":
    print_hi("PyCharm")
# Question 5
from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def read(self, filename):
        pass

    @abstractmethod
    def write(self, filename, data):
        pass


class TextFileHandler(FileHandler):
    def read(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()
        print(f"[TextFileHandler] Reading from {filename}")
        return data

    def write(self, filename, data):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(data)
        print(f"[TextFileHandler] Writing to {filename}")


class BinaryFileHandler(FileHandler):
    def read(self, filename):
        with open(filename, "rb") as f:
            data = f.read()
        print(f"[BinaryFileHandler] Reading from {filename}")
        return data

    def write(self, filename, data):
        with open(filename, "wb") as f:
            f.write(data)
        print(f"[BinaryFileHandler] Writing to {filename}")


if '_name_'== "_main_":
    text_handler = TextFileHandler()
    binary_handler = BinaryFileHandler()

    text_handler.write("example.txt", "Hello, Abstract Base Classes!")
    print(text_handler.read("example.txt"))

    binary_handler.write("example.bin", b"\x48\x65\x6C\x6C\x6F")
    print(binary_handler.read("example.bin"))