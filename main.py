  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import platform
def get_python_version():
        return platform.python_version()