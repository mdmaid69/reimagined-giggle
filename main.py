  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize