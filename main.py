  import math
  def calculate_square_root(n):
        return math.sqrt(n)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)