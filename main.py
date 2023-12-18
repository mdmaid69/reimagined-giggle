  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  def is_even(n):
        return n % 2 == 0