  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
def remove_duplicates(lst):
        return list(set(lst))