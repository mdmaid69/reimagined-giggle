  import sys
  def get_python_version():
        return sys.version
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)