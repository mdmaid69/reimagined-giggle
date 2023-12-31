import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)