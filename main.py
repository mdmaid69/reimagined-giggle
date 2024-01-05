  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)