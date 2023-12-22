  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
  def is_odd(n):
        return n % 2 != 0