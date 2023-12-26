def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"