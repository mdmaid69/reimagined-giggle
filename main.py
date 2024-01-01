  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import array
def get_array_as_int(array):
        return int(array[0])