  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)