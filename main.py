  import os
  def split_path(path):
        return os.path.split(path)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a