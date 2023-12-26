  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
def cube_number(x):
        return x**3