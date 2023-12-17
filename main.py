  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]