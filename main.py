import array
def get_array_as_frozenset(array):
        return frozenset(array)
  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks