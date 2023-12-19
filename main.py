  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import sys
def add_to_python_path(path):
        sys.path.append(path)