import platform
def get_os_info():
        return platform.uname()
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)