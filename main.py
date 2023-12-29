def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)