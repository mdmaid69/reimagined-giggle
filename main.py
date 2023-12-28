import platform
def get_os_info():
        return platform.uname()
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size