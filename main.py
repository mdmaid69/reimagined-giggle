import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)