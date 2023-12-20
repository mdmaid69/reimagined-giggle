  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import os
def get_environment_variable(var):
        return os.getenv(var)