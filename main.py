  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import array
def get_array_item(array, i):
        return array[i]