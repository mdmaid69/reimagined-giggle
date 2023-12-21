  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)