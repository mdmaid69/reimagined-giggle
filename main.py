  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  def subtract_numbers(x, y):
        return x - y