  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import array
def get_array_item_count(array, item):
        return array.count(item)