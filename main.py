  import math
  def calculate_square_root(n):
        return math.sqrt(n)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))