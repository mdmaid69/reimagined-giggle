import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value