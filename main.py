  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import os
def get_file_size(filename):
        return os.path.getsize(filename)