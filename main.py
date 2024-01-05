  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a