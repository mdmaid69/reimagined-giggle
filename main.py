import math
def calculate_sign(x):
        return math.copysign(1, x)
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True