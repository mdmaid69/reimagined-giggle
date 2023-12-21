  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import platform
def get_os_info():
        return platform.uname()