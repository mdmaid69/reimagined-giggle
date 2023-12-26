  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import array
def set_array_item(array, i, item):
        array[i] = item