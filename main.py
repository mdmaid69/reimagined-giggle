  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import array
def remove_from_array(array, item):
        array.remove(item)