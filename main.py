def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)