import platform
def get_os_info():
        return platform.uname()
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)