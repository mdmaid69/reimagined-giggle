  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)