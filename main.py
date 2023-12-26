  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
def cube_number(x):
        return x**3