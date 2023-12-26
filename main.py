  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import platform
def get_python_version():
        return platform.python_version()