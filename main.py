  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable