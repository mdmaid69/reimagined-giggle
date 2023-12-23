  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
  def is_even(n):
        return n % 2 == 0