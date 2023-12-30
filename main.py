import math
def calculate_ceiling(x):
        return math.ceil(x)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))