  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import platform
def get_os_info():
        return platform.uname()