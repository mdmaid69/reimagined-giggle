def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"