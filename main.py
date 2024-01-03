  import os
  def get_base_name(path):
        return os.path.basename(path)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)