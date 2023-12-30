  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import array
def extend_array(array, iterable):
        array.extend(iterable)