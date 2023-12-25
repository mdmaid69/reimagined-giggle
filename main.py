  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time