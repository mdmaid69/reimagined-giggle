  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import os
def get_environment_variable(var):
        return os.getenv(var)