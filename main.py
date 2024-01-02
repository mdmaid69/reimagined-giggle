import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)