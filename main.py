  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)