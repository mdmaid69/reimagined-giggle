  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time