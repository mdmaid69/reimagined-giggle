  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import os
def get_environment_variable(var):
        return os.getenv(var)