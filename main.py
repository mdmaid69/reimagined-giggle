  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)