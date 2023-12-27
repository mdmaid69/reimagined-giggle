  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import array
def extend_array(array, iterable):
        array.extend(iterable)