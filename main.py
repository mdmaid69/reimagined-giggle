  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import sys
def add_to_python_path(path):
        sys.path.append(path)