  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value