  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)