def convert_to_octal(n):
        return oct(n)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize