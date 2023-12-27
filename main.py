  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
def is_odd(n):
        return n % 2 != 0