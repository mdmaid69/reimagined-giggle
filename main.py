  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import sys
def print_python_version():
        return sys.version