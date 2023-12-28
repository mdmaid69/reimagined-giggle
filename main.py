  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import array
def get_list_from_array(array):
        return array.tolist()