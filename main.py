def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize