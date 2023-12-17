import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)