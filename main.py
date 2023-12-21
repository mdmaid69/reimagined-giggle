  import os
  def split_path(path):
        return os.path.split(path)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)