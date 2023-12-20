  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time