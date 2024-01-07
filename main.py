  import os
  def split_path(path):
        return os.path.split(path)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value