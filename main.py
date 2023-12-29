  import os
  def split_path(path):
        return os.path.split(path)
import platform
def get_os_info():
        return platform.uname()