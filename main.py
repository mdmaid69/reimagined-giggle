import math
def calculate_logarithm(base, x):
        return math.log(x, base)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)