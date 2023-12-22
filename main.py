import platform
def get_os_info():
        return platform.uname()
  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime