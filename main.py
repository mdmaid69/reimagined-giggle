  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import platform
def get_os_info():
        return platform.uname()