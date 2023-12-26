import math
def calculate_exponential(x):
        return math.exp(x)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)