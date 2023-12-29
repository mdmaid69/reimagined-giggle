  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import array
def remove_from_array(array, item):
        array.remove(item)