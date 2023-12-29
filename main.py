def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True