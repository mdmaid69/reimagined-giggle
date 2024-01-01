  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array