  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import os
def get_environment_variable(var):
        return os.getenv(var)