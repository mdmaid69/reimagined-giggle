  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import array
def convert_array_to_bytes(array):
        return array.tobytes()