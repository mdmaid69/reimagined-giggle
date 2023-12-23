  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import array
def pop_from_array(array, i=-1):
        return array.pop(i)