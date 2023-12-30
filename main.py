  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))