  import os
  def split_path(path):
        return os.path.split(path)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable