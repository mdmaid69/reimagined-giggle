import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import math
def calculate_absolute_value(x):
        return math.fabs(x)