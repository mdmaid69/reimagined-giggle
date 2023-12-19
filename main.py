import platform
def get_python_version():
        return platform.python_version()
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)