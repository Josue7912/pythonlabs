'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''
class Vehicle:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self):
        return f"My {self.model} was build in {self.year} and its maximum speed is {self.max_speed} km/h."

class Truck(Vehicle):

    def __init__(self, model, year, max_speed, load):
        super().__init__(model, year, max_speed)
        self.load = load

    def __str__(self):
        return f"My {self.model} truck from {self.year} can carry up to {self.load}KG"

class Motorcycle(Vehicle):

    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self):
        return f"The {self.model} motorbike can run up to {self.max_speed}km/h and it's from {self.year}"

mycar = Vehicle("Citroen", "2018", 220)
mytruck = Truck("Renault", "2001", 140, 2400)
mymoto = Motorcycle("Yamaha", "2010", 300)
print(mycar)
print(mytruck)
print(mymoto)