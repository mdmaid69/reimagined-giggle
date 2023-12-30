  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import sys
def print_python_version():
        print(sys.version)