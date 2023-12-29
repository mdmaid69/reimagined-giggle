import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import sys
  def get_python_version():
        return sys.version