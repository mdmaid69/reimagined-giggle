import sys
def add_to_python_path(path):
        sys.path.append(path)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)