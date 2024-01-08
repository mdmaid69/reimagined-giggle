  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import sys
def add_to_python_path(path):
        sys.path.append(path)