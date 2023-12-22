def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"