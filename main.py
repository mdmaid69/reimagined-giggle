  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import array
def get_array_as_frozenset(array):
        return frozenset(array)