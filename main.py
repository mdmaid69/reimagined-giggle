  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a