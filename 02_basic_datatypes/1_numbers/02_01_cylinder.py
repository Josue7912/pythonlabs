'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
radius = 3.14
height = 5
pi = 3.1416
vol = pi * radius * radius * height
area_l = 2 * pi * radius * height
area = area_l + 2 * pi * radius * radius
print(f"volumen is: {vol}")
print(f"surface area is: {area}")