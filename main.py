  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import array
def get_array_index(array, item):
        return array.index(item)