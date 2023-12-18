  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}