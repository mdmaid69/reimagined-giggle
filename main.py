  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time