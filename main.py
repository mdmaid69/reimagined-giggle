import array
def get_array_item_count(array, item):
        return array.count(item)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize