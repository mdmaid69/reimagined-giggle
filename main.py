  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)