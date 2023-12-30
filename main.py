  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)