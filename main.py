  import os
  def get_current_working_directory():
        return os.getcwd()
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value