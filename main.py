import platform
def get_os_info():
        return platform.uname()
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)