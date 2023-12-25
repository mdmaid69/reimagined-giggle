  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)