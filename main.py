import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)