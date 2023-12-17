  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
def cube_number(x):
        return x**3