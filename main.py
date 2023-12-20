  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value