import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))