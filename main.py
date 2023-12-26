  import os
  def delete_file(file_name):
        os.remove(file_name)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a