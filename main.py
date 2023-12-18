  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import platform
def get_os_info():
        return platform.uname()