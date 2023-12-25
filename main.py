  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import platform
def get_os_info():
        return platform.uname()