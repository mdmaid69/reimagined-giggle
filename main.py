  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import sys
def print_python_version():
        print(sys.version)