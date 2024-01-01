import platform
def get_os_info():
        return platform.uname()
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)