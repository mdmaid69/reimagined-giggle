  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
  import os
  def get_base_name(path):
        return os.path.basename(path)