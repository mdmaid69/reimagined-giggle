  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps