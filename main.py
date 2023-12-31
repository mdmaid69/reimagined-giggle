import math
def calculate_gamma_function(x):
        return math.gamma(x)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)