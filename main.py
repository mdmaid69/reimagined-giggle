import os
def get_environment_variable(var):
        return os.getenv(var)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)