  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
  def add_numbers(x, y):
        return x + y