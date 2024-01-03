  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a