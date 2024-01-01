import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))