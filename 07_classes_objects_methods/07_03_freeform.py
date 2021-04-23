'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''
class Trousers:
    def __init__(self, color, pattern, size):
        self.color = color
        self.pattern = pattern
        self.size = size

    def __add__(self, newcolor):
        return Trousers(self.color + newcolor.color)

    def __str__(self):
        return f"This {self.size} {self.pattern} {self.color} trouser fits me"

class Shoes:
    def __init__(self, color, brand, size):
        self.color = color
        self.brand = brand
        self.size = size

    def __str__(self):
        return f"Today I'm going to wear the {self.size} {self.color} {self.brand} shoes"

class TShirt:
    def __init__(self, color, material, size):
        self.color = color
        self.material = material
        self.size = size

    def __str__(self):
        return f"This {self.size} {self.color} {self.material} T-Shirt combines with my trousers and shoes"

shoe1 = Shoes("blue", "Nike", "42")
shoe2 = Shoes("white", "Adidas", "38")
trou1 = Trousers("black", "plain", "L-size")
trou2 = Trousers("blue", "striped", "XL-size")
tshi1 = TShirt("white", "cotton", "L-size")
tshi2 = TShirt("grey", "licra", "S-size")
print(shoe1)
print(shoe2)
print(trou1)
print(trou2)
print(tshi1)
print(tshi2)
