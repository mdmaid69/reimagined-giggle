  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)