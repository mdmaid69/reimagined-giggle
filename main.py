  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value