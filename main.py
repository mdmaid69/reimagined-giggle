  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)