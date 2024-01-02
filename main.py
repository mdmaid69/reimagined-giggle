import os
def list_files_in_directory(path):
        return os.listdir(path)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value