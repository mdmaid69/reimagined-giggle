import math
def calculate_sign(x):
        return math.copysign(1, x)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)