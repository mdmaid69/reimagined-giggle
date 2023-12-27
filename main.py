import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)