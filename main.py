import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"