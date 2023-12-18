  import os
  def get_directory_name(path):
        return os.path.dirname(path)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value