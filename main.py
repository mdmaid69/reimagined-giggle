  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import os
def get_environment_variable(var):
        return os.getenv(var)