  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import array
def get_array_itemsize(array):
        return array.itemsize