  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a