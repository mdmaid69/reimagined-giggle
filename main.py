  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import array
def get_array_as_int(array):
        return int(array[0])