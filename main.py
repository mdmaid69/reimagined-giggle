  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import sys
def add_to_python_path(path):
        sys.path.append(path)