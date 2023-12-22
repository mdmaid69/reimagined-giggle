import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)