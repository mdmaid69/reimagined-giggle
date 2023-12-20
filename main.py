  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import array
def remove_from_array(array, item):
        array.remove(item)