import os
def remove_directory(path):
        os.rmdir(path)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)