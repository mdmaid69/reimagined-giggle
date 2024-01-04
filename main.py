  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import platform
def get_os_info():
        return platform.uname()