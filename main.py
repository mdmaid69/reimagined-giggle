  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def calculate_average(lst):
        return sum(lst) / len(lst)