  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a