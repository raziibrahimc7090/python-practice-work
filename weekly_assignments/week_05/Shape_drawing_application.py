from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def draw(self):
        print("Drawing Circle")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def draw(self):
        print("Drawing Rectangle")


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def draw(self):
        print("Drawing Triangle")


circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

circle.draw()
print(f"Circle Area: {circle.area():.2f}")

rectangle.draw()
print(f"Rectangle Area: {rectangle.area()}")

triangle.draw()
print(f"Triangle Area: {triangle.area()}")