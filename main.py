  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a