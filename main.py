  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import array
def reverse_array(array):
        array.reverse()