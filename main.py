  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)