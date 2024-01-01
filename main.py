import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)