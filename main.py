  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)