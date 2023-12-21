import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)