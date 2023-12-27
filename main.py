  import sys
  def get_python_version():
        return sys.version
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value