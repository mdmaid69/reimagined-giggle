import sys
def print_python_version():
        return sys.version
  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev