import sys
def print_python_version():
        print(sys.version)
  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino