import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)