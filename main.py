  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
  def add_numbers(x, y):
        return x + y