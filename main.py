def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import math
def calculate_circle_area(radius):
        return math.pi * radius**2