import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)