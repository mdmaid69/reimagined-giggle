  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import sys
def add_to_python_path(path):
        sys.path.append(path)