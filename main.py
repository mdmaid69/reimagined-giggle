  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))