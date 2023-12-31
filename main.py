  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a