  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import array
def remove_from_array(array, item):
        array.remove(item)