import platform
def get_python_version():
        return platform.python_version()
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)