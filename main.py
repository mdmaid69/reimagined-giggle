import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)