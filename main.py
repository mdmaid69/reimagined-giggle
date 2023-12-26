  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  import sys
  def get_python_version():
        return sys.version