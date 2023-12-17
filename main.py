  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)