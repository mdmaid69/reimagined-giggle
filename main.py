  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import array
def set_array_item(array, i, item):
        array[i] = item