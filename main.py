  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  def cube_number(x):
        return x**3