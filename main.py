def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"