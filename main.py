  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
  def is_even(n):
        return n % 2 == 0