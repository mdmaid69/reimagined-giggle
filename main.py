  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a