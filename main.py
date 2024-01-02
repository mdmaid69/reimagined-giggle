import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)