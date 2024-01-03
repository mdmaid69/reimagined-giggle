  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import array
def insert_into_array(array, i, item):
        array.insert(i, item)