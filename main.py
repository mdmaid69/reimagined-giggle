  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)