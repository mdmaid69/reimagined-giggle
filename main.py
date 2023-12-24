  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import array
def set_array_item(array, i, item):
        array[i] = item