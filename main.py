  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a