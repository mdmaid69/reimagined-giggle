  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import array
def insert_into_array(array, i, item):
        array.insert(i, item)