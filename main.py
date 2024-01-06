import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)