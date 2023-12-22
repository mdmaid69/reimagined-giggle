  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import platform
def get_python_version():
        return platform.python_version()