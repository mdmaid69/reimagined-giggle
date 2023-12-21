def sort_list(lst):
        return sorted(lst)
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize