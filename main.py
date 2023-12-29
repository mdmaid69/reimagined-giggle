import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)