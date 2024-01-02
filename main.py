import platform
def get_os_info():
        return platform.uname()
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)