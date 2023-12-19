import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)