  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
def cube_number(x):
        return x**3