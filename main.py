  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
  def subtract_numbers(x, y):
        return x - y