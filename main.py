  def is_even(n):
        return n % 2 == 0
  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns