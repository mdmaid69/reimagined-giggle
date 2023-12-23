import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius