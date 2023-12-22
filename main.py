import array
def get_array_as_memoryview(array):
        return memoryview(array)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)