import math
def calculate_error_function(x):
        return math.erf(x)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)