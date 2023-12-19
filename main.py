  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import platform
def get_python_version():
        return platform.python_version()