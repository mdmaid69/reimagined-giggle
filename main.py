  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a