  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value