  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)