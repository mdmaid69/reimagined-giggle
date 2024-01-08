import sys
def add_to_python_path(path):
        sys.path.append(path)
  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino