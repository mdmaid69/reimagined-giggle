import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)