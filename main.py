  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import platform
def get_python_version():
        return platform.python_version()