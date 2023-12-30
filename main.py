  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import array
def append_to_array(array, item):
        array.append(item)