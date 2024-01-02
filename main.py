import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))