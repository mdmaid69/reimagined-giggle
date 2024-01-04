  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
def multiply_numbers(x, y):
        return x * y