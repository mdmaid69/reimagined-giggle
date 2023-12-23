  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a