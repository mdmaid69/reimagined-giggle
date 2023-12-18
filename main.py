  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value