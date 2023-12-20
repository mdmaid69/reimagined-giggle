  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import sys
def add_to_python_path(path):
        sys.path.append(path)