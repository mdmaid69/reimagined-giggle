def is_odd(n):
        return n % 2 != 0
  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid