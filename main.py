  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import sys
def add_to_python_path(path):
        sys.path.append(path)