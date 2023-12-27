  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import array
def insert_into_array(array, i, item):
        array.insert(i, item)