  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import os
def get_environment_variable(var):
        return os.getenv(var)