  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)