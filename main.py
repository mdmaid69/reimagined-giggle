  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a