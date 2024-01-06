import array
def get_array_typecode(array):
        return array.typecode
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size