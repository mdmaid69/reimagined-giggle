import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"