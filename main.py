  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a