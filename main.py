  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
  def is_odd(n):
        return n % 2 != 0