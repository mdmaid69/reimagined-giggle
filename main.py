import sys
def add_to_python_path(path):
        sys.path.append(path)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)