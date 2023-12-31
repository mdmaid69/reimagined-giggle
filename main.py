import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))