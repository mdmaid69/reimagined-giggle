  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
  def cube_number(x):
        return x**3