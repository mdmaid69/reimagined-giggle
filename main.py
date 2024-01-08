  def convert_to_octal(n):
        return oct(n)
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize