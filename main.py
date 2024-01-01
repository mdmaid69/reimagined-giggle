import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)