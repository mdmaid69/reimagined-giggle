  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import os
def get_environment_variable(var):
        return os.getenv(var)