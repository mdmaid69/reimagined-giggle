import array
def get_array_as_frozenset(array):
        return frozenset(array)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]