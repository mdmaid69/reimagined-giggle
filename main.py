  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import array
def append_to_array(array, item):
        array.append(item)