  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a