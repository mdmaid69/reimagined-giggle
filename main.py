  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import platform
def get_python_version():
        return platform.python_version()