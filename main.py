  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import array
def insert_into_array(array, i, item):
        array.insert(i, item)