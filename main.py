  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
  def convert_to_hex(n):
        return hex(n)