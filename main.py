  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import array
def insert_into_array(array, i, item):
        array.insert(i, item)