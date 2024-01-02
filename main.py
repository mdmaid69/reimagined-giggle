  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize