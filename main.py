  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)