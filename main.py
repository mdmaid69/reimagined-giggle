  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import sys
def add_to_python_path(path):
        sys.path.append(path)