  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import array
def set_array_item(array, i, item):
        array[i] = item