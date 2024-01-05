import sys
def print_python_version():
        print(sys.version)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)