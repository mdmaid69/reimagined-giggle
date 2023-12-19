import array
def get_array_item_count(array, item):
        return array.count(item)
  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks