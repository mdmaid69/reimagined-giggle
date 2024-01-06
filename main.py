  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable