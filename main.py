  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable