  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import sys
def add_to_python_path(path):
        sys.path.append(path)