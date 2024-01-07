import platform
def get_os_info():
        return platform.uname()
  import os
  def get_base_name(path):
        return os.path.basename(path)