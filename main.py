import platform
def get_python_version():
        return platform.python_version()
  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime