  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
  def is_even(n):
        return n % 2 == 0