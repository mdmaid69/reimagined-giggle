  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import os
def get_environment_variable(var):
        return os.getenv(var)