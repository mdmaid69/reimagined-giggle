  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a