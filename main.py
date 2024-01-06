import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)