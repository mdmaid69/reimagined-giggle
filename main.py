  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable