  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import sys
def add_to_python_path(path):
        sys.path.append(path)