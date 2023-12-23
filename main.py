def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height