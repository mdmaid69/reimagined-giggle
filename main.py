  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import array
def get_array_as_tuple(array):
        return tuple(array)