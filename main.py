import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True