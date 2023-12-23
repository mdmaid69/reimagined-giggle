  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import sys
def print_python_version():
        return sys.version