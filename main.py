  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import array
def set_array_item(array, i, item):
        array[i] = item