  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable