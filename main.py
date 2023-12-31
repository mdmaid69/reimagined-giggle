import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)