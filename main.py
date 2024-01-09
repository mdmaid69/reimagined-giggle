import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)