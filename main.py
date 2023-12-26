import array
def insert_into_array(array, i, item):
        array.insert(i, item)
  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks