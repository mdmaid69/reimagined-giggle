  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)