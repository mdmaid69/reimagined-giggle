import math
def calculate_circle_area(radius):
        return math.pi * radius**2
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))