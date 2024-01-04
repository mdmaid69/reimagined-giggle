  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a