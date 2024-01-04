import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))