  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a