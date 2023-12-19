  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import getpass
def get_username():
        return getpass.getuser()