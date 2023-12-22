import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  def remove_duplicates(lst):
        return list(set(lst))