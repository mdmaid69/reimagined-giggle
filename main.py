  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a