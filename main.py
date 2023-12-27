  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
def is_odd(n):
        return n % 2 != 0