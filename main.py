  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import platform
def get_python_version():
        return platform.python_version()