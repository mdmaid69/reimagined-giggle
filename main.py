import sys
def print_python_version():
        print(sys.version)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)