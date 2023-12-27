import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)