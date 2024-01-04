  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
  def is_odd(n):
        return n % 2 != 0