import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))