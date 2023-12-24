  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import array
def set_array_item(array, i, item):
        array[i] = item