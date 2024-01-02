  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)