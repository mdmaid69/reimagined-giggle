  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
  def square_number(x):
        return x**2