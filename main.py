import math
def calculate_sign(x):
        return math.copysign(1, x)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)