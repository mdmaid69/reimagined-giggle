  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import array
def remove_from_array(array, item):
        array.remove(item)