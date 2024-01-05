import math
def calculate_square_root(x):
        return math.sqrt(x)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)