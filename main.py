  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value