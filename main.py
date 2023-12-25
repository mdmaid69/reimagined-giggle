import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)