  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)