  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable