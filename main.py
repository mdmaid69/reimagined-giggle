  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)