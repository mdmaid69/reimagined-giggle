import array
def get_array_as_tuple(array):
        return tuple(array)
  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size