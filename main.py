  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import array
def insert_into_array(array, i, item):
        array.insert(i, item)