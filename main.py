  import sys
  def get_python_version():
        return sys.version
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime