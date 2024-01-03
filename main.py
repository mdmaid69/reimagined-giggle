  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
  def cube_number(x):
        return x**3