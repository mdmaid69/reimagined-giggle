  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import platform
def get_python_version():
        return platform.python_version()