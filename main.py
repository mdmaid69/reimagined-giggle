import platform
def get_os_info():
        return platform.uname()
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)