def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True