  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
def divide_numbers(x, y):
        return x / y