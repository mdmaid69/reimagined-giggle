import platform
def get_python_version():
        return platform.python_version()
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)