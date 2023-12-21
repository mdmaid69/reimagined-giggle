  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import array
def get_array_typecode(array):
        return array.typecode