import math
def calculate_error_function(x):
        return math.erf(x)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)