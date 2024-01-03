  import os
  def get_current_working_directory():
        return os.getcwd()
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable