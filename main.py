  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import array
def get_array_length(array):
        return len(array)