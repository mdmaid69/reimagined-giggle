  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import sys
def add_to_python_path(path):
        sys.path.append(path)