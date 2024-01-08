  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
  import os
  def delete_file(file_name):
        os.remove(file_name)