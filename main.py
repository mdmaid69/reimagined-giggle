  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import array
def set_array_item(array, i, item):
        array[i] = item