  import sys
  def get_python_version():
        return sys.version
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)