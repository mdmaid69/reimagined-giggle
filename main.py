  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
def remove_duplicates(lst):
        return list(set(lst))