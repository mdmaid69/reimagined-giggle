  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import sys
def print_python_version():
        return sys.version