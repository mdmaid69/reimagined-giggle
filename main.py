import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import math
def calculate_error_function(x):
        return math.erf(x)