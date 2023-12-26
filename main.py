  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import array
def remove_from_array(array, item):
        array.remove(item)