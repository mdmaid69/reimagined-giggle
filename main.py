  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import os
def get_environment_variable(var):
        return os.getenv(var)