  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import array
def get_array_as_bytes(array):
        return bytes(array)