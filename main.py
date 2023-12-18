  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value