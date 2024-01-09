import math
def calculate_ceiling(x):
        return math.ceil(x)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)