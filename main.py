  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import os
def get_environment_variable(var):
        return os.getenv(var)