  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import sys
def print_python_version():
        print(sys.version)