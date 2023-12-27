import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)