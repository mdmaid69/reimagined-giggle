  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)