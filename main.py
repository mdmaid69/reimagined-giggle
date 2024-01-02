def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True
  def calculate_circumference_circle(r):
        return 2 * 3.14 * r