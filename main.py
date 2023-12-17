  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a