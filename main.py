import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value