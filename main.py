  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a