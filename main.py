import array
def get_list_from_array(array):
        return array.tolist()
  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks