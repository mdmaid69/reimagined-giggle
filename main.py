import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  def remove_duplicates(lst):
        return list(set(lst))