  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import array
def set_array_item(array, i, item):
        array[i] = item