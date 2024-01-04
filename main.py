  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable