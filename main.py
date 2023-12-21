  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)