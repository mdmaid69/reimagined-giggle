  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
def add_numbers(x, y):
        return x + y