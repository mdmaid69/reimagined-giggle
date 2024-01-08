  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
  def cube_number(x):
        return x**3