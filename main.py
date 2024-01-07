import re
def split_string(pattern, string):
        return re.split(pattern, string)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"