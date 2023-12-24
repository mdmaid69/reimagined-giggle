  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a