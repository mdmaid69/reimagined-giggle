  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a