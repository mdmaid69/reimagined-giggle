  import os
  def get_current_directory():
        return os.getcwd()
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a