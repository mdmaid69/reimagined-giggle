  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time