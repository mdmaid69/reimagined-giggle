  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import platform
def get_os_info():
        return platform.uname()