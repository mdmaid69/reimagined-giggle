  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import os
def get_environment_variable(var):
        return os.getenv(var)