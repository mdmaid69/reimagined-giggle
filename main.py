  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius