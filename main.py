import platform
def get_python_version():
        return platform.python_version()
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)