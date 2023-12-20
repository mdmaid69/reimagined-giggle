import math
def calculate_factorial(n):
        return math.factorial(n)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))