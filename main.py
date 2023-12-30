import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)