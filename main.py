  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import array
def set_array_item(array, i, item):
        array[i] = item