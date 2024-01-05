import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"