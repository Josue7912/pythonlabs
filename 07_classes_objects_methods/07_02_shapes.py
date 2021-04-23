'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perim(self):
        return 2 * (self.length + self.width)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * 3.14

    def circum(self):
        return 2 * 3.14 * self.radius

rec = Rectangle(4, 5)
cir = Circle(3)
print(rec.area())
print(rec.perim())
print(cir.area())
print(cir.circum())
