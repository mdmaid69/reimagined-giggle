import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))