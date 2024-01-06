import platform
def get_python_version():
        return platform.python_version()
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)