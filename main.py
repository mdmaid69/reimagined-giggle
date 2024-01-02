  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import array
def get_array_as_frozenset(array):
        return frozenset(array)