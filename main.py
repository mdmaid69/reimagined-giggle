import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)