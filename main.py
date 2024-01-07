  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
  import sys
  def get_python_version():
        return sys.version