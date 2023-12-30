  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import sys
def print_python_version():
        return sys.version