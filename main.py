  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import platform
def get_os_info():
        return platform.uname()