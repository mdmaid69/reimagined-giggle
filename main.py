  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)