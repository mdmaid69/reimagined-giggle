import math
def calculate_error_function(x):
        return math.erf(x)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)