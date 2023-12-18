def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
  def calculate_perimeter_triangle(a, b, c):
        return a + b + c