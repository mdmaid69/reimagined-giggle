  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import sys
def add_to_python_path(path):
        sys.path.append(path)