  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)