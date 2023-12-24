import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)