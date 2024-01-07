  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value