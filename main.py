import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True