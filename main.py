  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  def square_number(x):
        return x**2