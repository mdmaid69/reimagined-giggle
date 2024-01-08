import getpass
def get_username():
        return getpass.getuser()
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)