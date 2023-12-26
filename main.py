def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True