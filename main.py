  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import array
def get_array_as_set(array):
        return set(array)