  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import array
def get_array_item_count(array, item):
        return array.count(item)