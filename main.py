import math
def calculate_absolute_value(x):
        return math.fabs(x)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)