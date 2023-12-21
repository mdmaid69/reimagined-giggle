  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)