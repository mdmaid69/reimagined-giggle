  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a