  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import array
def get_array_as_frozenset(array):
        return frozenset(array)