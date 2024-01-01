  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import array
def convert_array_to_bytes(array):
        return array.tobytes()