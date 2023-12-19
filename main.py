  import os
  def get_base_name(path):
        return os.path.basename(path)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable