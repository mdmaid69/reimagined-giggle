  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"