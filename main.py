  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a