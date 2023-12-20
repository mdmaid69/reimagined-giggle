import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value