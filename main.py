  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import array
def get_array_slice(array, i, j):
        return array[i:j]