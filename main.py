  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)