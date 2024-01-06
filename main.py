import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)