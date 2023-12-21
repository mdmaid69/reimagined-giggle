import platform
def get_os_info():
        return platform.uname()
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)