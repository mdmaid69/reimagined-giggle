  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
  def is_even(n):
        return n % 2 == 0