  import sys
  def get_python_version():
        return sys.version
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)