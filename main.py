  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)