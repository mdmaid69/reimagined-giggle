def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)