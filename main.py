import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)