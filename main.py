  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps