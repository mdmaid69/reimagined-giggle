  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
def square_number(x):
        return x**2