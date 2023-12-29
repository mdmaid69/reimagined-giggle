import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)