  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value