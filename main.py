  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)