  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import sys
def add_to_python_path(path):
        sys.path.append(path)