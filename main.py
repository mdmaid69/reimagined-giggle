  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import os
def get_environment_variable(var):
        return os.getenv(var)