import os
def get_environment_variable(var):
        return os.getenv(var)
  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode