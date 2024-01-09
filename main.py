  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)