  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)