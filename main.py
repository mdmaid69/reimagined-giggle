  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import sys
def add_to_python_path(path):
        sys.path.append(path)