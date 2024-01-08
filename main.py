import sys
def add_to_python_path(path):
        sys.path.append(path)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]