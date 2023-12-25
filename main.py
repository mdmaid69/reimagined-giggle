  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import platform
def get_python_version():
        return platform.python_version()