  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
  def calculate_circumference_circle(r):
        return 2 * 3.14 * r