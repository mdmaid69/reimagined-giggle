  def calculate_area_circle(r):
        return 3.14 * r**2
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True