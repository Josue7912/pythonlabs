'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():
    def __init__(self, name, colour, solarsystem):
        self.name = name
        self.colour = colour
        self.solarsystem = solarsystem

    def __str__(self):
        return f"Planet {self.name} is a {self.colour} planet and its part of the {self.solarsystem}."

earth = Planet("Earth", "Blue", "Solar System")
print(earth)
