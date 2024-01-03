  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a