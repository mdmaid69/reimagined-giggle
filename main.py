import math
def calculate_factorial(n):
        return math.factorial(n)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)