  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import platform
def get_os_info():
        return platform.uname()