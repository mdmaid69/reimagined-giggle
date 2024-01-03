  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a