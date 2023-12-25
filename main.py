import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)