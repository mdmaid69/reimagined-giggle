  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
  def calculate_area_triangle(b, h):
        return 0.5 * b * h