def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))