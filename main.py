import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)