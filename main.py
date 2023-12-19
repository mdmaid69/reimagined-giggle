  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a