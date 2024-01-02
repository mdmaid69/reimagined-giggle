  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import array
def iterate_over_array(array):
        for item in array:
        print(item)