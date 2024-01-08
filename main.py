  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import array
def set_array_item(array, i, item):
        array[i] = item