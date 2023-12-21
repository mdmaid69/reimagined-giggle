  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
def cube_number(x):
        return x**3