  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import platform
def get_python_version():
        return platform.python_version()