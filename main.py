import platform
def get_python_version():
        return platform.python_version()
  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen