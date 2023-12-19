  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import array
def remove_from_array(array, item):
        array.remove(item)