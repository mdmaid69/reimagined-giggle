import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value