  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
  def cube_number(x):
        return x**3