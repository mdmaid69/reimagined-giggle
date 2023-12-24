  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import array
def append_to_array(array, item):
        array.append(item)