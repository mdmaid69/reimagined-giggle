import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"