  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
def is_odd(n):
        return n % 2 != 0