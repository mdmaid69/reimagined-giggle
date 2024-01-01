  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value