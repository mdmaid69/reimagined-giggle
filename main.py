import platform
def get_os_info():
        return platform.uname()
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]