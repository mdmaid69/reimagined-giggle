  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import os
def get_environment_variable(var):
        return os.getenv(var)