  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
def cube_number(x):
        return x**3