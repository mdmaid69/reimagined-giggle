import sys
def add_to_python_path(path):
        sys.path.append(path)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)