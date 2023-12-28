  import os
  def split_path(path):
        return os.path.split(path)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)