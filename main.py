  import os
  def get_base_name(path):
        return os.path.basename(path)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a