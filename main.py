import math
def calculate_sign(x):
        return math.copysign(1, x)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))