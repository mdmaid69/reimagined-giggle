import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))