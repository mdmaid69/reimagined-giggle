import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)