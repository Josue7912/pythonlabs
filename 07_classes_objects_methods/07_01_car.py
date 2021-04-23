'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''
class Car:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def accelerate(self, speed):
        self.max_speed = self.max_speed + speed

    def __str__(self):
        return f"My {self.model} was build in {self.year} and its maximum speed is {self.max_speed} km/h."

my_car1 = Car("Citroen", "2018", 220)
my_car2 = Car("Renault", "2001", 250)
print(my_car1)
print(my_car2)
my_car1.accelerate(5)
print(my_car1)
print(my_car2)