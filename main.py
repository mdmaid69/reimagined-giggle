  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
  def is_odd(n):
        return n % 2 != 0