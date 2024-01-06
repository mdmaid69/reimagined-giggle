  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value