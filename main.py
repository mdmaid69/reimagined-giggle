  import os
  def delete_file(file_name):
        os.remove(file_name)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable