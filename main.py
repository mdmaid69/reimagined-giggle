  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import platform
def get_python_version():
        return platform.python_version()