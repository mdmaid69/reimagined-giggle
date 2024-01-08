import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)