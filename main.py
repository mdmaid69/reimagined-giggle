  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a