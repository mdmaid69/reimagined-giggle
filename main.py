  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
  def cube_number(x):
        return x**3