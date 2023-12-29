  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
  def is_even(n):
        return n % 2 == 0