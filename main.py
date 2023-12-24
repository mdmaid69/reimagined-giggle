  import sys
  def get_python_version():
        return sys.version
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)