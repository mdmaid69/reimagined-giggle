import os
def get_environment_variable(var):
        return os.getenv(var)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)