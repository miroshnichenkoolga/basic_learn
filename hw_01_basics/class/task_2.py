class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area()==other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
    def __ne__(self, other):
        return self.area() != other.area()

rectangle1 = Rectangle(1, 1)
rectangle2 = Rectangle(2, 2)
rectangle3 = Rectangle(2, 2)

print(rectangle1 == rectangle2)  # False
print(rectangle2 == rectangle3)  # True
print(rectangle1 < rectangle2)  # True
print(rectangle2 < rectangle3)  # False
print(rectangle2 <= rectangle3)  # True