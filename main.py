  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import sys
def print_python_version():
        print(sys.version)