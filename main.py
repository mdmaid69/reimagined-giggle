import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))