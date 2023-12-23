import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)