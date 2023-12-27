import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)