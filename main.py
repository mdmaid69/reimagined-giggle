import math
def calculate_logarithm(base, x):
        return math.log(x, base)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)