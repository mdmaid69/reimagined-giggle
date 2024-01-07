def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"