import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)