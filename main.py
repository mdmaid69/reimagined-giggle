  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import array
def set_array_item(array, i, item):
        array[i] = item