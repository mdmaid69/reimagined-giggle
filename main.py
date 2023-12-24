  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import array
def get_array_as_bytearray(array):
        return bytearray(array)