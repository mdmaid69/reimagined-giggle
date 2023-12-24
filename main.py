  import os
  def delete_file(file_name):
        os.remove(file_name)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a