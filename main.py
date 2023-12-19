import os
def list_files_in_directory(path):
        return os.listdir(path)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)