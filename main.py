  import sys
  def get_python_version():
        return sys.version
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)