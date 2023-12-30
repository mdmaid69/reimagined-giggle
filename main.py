  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value