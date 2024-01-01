import re
def split_string(pattern, string):
        return re.split(pattern, string)
  def remove_duplicates(lst):
        return list(set(lst))