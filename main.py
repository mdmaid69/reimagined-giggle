  import os
  def delete_file(file_name):
        os.remove(file_name)
import platform
def get_os_info():
        return platform.uname()