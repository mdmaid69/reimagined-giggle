  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import platform
def get_python_version():
        return platform.python_version()