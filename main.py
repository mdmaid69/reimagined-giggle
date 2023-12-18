import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)