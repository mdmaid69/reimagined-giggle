import os
def get_environment_variable(var):
        return os.getenv(var)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]