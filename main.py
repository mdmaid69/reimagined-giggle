import platform
def get_python_version():
        return platform.python_version()
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)