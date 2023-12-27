def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))