  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import sys
def print_python_version():
        print(sys.version)