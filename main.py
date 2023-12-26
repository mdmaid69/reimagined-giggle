import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True