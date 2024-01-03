import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)