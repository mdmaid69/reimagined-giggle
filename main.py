def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"