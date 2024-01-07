  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"