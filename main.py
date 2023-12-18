  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import platform
def get_os_info():
        return platform.uname()