  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import array
def set_array_item(array, i, item):
        array[i] = item