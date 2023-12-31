  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
  import sys
  def get_python_version():
        return sys.version