import os
def remove_directory(path):
        os.rmdir(path)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value