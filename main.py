  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size