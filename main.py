  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import array
def get_array_as_frozenset(array):
        return frozenset(array)