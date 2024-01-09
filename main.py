  import sys
  def get_python_version():
        return sys.version
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)