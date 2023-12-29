import os
def get_environment_variable(var):
        return os.getenv(var)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)