  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import sys
def add_to_python_path(path):
        sys.path.append(path)