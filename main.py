  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import platform
def get_python_version():
        return platform.python_version()