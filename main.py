import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid