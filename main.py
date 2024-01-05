import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)