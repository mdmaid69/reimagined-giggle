  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import sys
def add_to_python_path(path):
        sys.path.append(path)