  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import sys
def add_to_python_path(path):
        sys.path.append(path)