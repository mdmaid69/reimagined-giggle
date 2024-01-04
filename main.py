  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import platform
def get_os_info():
        return platform.uname()