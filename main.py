import platform
def get_os_info():
        return platform.uname()
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)