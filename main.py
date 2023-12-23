  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import sys
def print_python_version():
        print(sys.version)