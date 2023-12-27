  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import array
def insert_into_array(array, i, item):
        array.insert(i, item)