  import os
  def get_current_directory():
        return os.getcwd()
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a