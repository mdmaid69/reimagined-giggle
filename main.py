  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import platform
def get_os_info():
        return platform.uname()