  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)