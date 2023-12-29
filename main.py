  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
  def cube_number(x):
        return x**3