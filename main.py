  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)