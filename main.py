  import sys
  def get_python_version():
        return sys.version
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)