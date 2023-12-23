  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import platform
def get_os_info():
        return platform.uname()