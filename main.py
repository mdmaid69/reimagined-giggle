  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)