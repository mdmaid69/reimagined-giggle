  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import platform
def get_python_version():
        return platform.python_version()