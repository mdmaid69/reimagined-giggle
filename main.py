import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value