def reverse_string(s):
        return s[::-1]
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize