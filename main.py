  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)