  import sys
  def get_python_version():
        return sys.version
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)