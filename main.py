  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import array
def set_array_item(array, i, item):
        array[i] = item