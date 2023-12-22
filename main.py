import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)