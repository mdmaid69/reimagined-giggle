  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import array
def remove_from_array(array, item):
        array.remove(item)