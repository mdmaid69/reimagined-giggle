  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)