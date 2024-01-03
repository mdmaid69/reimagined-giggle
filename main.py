import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)