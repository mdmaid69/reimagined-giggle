  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value