import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)