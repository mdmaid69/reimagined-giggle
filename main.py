import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value