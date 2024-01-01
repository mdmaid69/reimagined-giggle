import math
def calculate_floor(x):
        return math.floor(x)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))