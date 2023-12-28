  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import array
def remove_from_array(array, item):
        array.remove(item)