import sys
def print_python_version():
        print(sys.version)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)