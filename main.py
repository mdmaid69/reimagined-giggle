def calculate_area(radius):
        return 3.14 * radius * radius
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize