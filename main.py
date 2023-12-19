  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True
  def calculate_area_triangle(b, h):
        return 0.5 * b * h