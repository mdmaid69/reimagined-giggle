  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import array
def get_list_from_array(array):
        return array.tolist()