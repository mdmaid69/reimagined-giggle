  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import platform
def get_os_info():
        return platform.uname()