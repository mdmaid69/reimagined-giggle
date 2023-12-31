import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value