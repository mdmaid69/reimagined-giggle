  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
  def is_even(n):
        return n % 2 == 0