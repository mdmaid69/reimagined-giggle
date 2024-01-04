import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)