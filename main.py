  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import array
def get_array_as_set(array):
        return set(array)