  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import platform
def get_os_info():
        return platform.uname()