  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)