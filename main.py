import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))