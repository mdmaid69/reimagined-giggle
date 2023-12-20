import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))