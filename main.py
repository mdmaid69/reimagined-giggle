  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import array
def remove_from_array(array, item):
        array.remove(item)