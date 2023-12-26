  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import platform
def get_os_info():
        return platform.uname()