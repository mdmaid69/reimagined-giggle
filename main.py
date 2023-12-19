  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import sys
def add_to_python_path(path):
        sys.path.append(path)