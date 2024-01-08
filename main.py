  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"